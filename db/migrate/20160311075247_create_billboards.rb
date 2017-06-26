class CreateBillboards < ActiveRecord::Migration
  def change
    create_table :billboards do |t|
      t.string :image
      t.string :name
      t.string :rank
      t.string :share

      t.timestamps null: false
    end
  end
end
