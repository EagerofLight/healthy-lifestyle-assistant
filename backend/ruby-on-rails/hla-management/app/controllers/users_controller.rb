include Pundit

class UsersController < ApplicationController
  def index
    authorize User
    @users = User.all
    render json: @users
  end

  def show
    user = User.find(params[:id]) # find user
    authorize user # find permission
    render json: user # return json
  end

  def update
    user = User.find(params[:id])
    authorize user
    if user.update(user_params)
      render json: user
    else
      render json: { error: user.errors }, status: :unprocessable_entity
    end
  end

  def destroy
    user = User.find(params[:id])
    authorize user
    user.destroy
    head :no_content
  end

  private
  def user_params
    params.require(:user).permit(:name, :email, :role, :status, :password)
  end
end
