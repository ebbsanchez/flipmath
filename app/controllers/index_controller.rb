class IndexController < ApplicationController
	def home
		@billboards = Billboard.all
	end
end
