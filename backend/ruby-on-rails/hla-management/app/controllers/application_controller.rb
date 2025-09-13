class ApplicationController < ActionController::API
  include Pundit::Authorization

  before_action :authenticate_user! # ! means important

  # have more 
  before_action :configure_permitted_parameters, if: :devise_controller?

  protected

  def configure_permitted_parameters
    devise_parameter_sanitizer.permit(:sign_up, keys: [:name])
    devise_parameter_sanitizer.permit(:account_update, keys: [:name])
  end

  rescue_from Pundit::NotAuthorizedError, with: :user_not_authorized

  private

  def user_not_authorized(exception)
    render json: { error: "You are not authorized to perform this action" }, status: :forbidden
  end
end
