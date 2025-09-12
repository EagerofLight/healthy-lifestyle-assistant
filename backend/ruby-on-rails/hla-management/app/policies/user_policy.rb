class UserPolicy < ApplicationPolicy
  ## Record -> object you wanna operate
  ## User -> object you are
  def index?
    user.admin? # only admin can check user list
  end

  def show?
    user.admin? || record.id == user.id # admin can check others, user only check self
  end

  def update?
    user.admin? || record.id == user.id # same
  end

  def destroy?
    user.super_admin? # only super admin
  end
end