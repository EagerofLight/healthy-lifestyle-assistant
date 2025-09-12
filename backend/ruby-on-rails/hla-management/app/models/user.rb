class User < ApplicationRecord # base Model
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable
  devise :database_authenticatable, # email + pwd login
         :registerable, # register + login
         :recoverable,  # recover pwd
         :rememberable, # remember me
         :validatable, # validate email & pwd
         :jwt_authenticatable, # use jwt login
         jwt_revocation_strategy: self
  
  # revocation: use jti
  include Devise::JWT::RevocationStrategies::JTIMatcher

  after_initialize :set_default_role, if: :new_record? # rails callback, do after initilization
  # if: :new_record? -> only trigger when new record is triggered (true -> new object)

  def set_default_role
    self.role ||= 'user' # ||= -> if is null then setter
  end

  def admin? # ? -. return bool
    role == 'admin' || role == 'super_admin'
  end

  def super_admin?
    role == 'super_admin'
  end
end
