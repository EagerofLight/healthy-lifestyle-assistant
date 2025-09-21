class AddJtiToUsers < ActiveRecord::Migration[8.0]
  def change
    add_column :users, :jti, :uuid
    add_index :users, :jti
  end
end
