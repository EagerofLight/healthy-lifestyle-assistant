# frozen_string_literal: true

class Users::SessionsController < Devise::SessionsController
  # before_action :configure_sign_in_params, only: [:create]

  respond_to :json

  private

  def respond_with(resource, _opts = {})
    render json: { message: 'Logged in successfully.', user: resource }, status: :ok
  end

  def respond_to_on_destroy
    render json: { message: 'Logged out successfully.' }, status: :ok
  end

  def current_token
    request.env['warden-jwt_auth.token']
  end
  # GET /resource/sign_in
  # def new
  #   super
  # end

  # POST /resource/sign_in
  # def create
  #   super
  # end

  # DELETE /resource/sign_out
  # def destroy
  #   super
  # end

  # protected

  # If you have extra params to permit, append them to the sanitizer.
  # def configure_sign_in_params
  #   devise_parameter_sanitizer.permit(:sign_in, keys: [:attribute])
  # end
end
