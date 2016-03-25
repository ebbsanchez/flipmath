class AddSchoolToBillboards < ActiveRecord::Migration
  def change
  	add_column :billboards, :school, :string, :after => :name
  end
end
