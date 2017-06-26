source 'https://rubygems.org'

<<<<<<< HEAD
# Trick to use https without warnings and without having to specify full URLs
# TODO: Can be removed when Bundler 2.x is released.
git_source(:github) do |repo_name|
  repo_name = "#{repo_name}/#{repo_name}" unless repo_name.include?("/")
  "https://github.com/#{repo_name}.git"
end

# Optional dependencies
gem 'cancan'
gem 'pundit'

# Utility gems used in both development & test environments
gem 'rake'
gem 'parallel_tests'

# Debugging
gem 'pry' # Easily debug from your console with `binding.pry`

# Code style
gem 'rubocop', '0.49.1'
gem 'mdl', '0.4.0'

# Translations
gem 'i18n-tasks'

group :development do
  # Debugging
  gem 'better_errors' # Web UI to debug exceptions. Go to /__better_errors to access the latest one

  gem 'binding_of_caller', platforms: :mri # Retrieve the binding of a method's caller

  # Performance
  gem 'rack-mini-profiler' # Inline app profiler. See ?pp=help for options.

  # Documentation
  gem 'yard'                        # Documentation generator
  gem 'redcarpet', platforms: :mri  # Markdown implementation (for yard)
  gem 'kramdown', platforms: :jruby # Markdown implementation (for yard)
end

group :test do
  gem 'capybara'
  gem 'simplecov', require: false # Test coverage generator. Go to /coverage/ after running tests
  gem 'codecov', require: false # Test coverage website. Go to https://codecov.io
  gem 'cucumber-rails', require: false
  gem 'cucumber'
  gem 'database_cleaner'
  gem 'jasmine'
  gem 'launchy'
  gem 'rails-i18n' # Provides default i18n for many languages
  gem 'rspec-rails'
  gem 'i18n-spec'
  gem 'shoulda-matchers', '<= 2.8.0'
  gem 'sqlite3', platforms: :mri
  gem 'poltergeist'
=======

# Bundle edge Rails instead: gem 'rails', github: 'rails/rails'
gem 'rails', '4.2.5.1'
# Use sqlite3 as the database for Active Record
# gem 'sqlite3'
# Use SCSS for stylesheets
gem 'sass-rails', '~> 5.0'
# Use Uglifier as compressor for JavaScript assets
gem 'uglifier', '>= 1.3.0'
# Use CoffeeScript for .coffee assets and views
gem 'coffee-rails', '~> 4.1.0'
# See https://github.com/rails/execjs#readme for more supported runtimes
# gem 'therubyracer', platforms: :ruby

# Use jquery as the JavaScript library
gem 'jquery-rails'
# Turbolinks makes following links in your web application faster. Read more: https://github.com/rails/turbolinks
gem 'turbolinks'
# Build JSON APIs with ease. Read more: https://github.com/rails/jbuilder
gem 'jbuilder', '~> 2.0'
# bundle exec rake doc:rails generates the API under doc/api.
gem 'sdoc', '~> 0.4.0', group: :doc

# Use ActiveModel has_secure_password
# gem 'bcrypt', '~> 3.1.7'

# Use Unicorn as the app server
# gem 'unicorn'

# Use Capistrano for deployment
# gem 'capistrano-rails', group: :development

 gem 'font-awesome-sass'
group :development, :test do
  # Call 'byebug' anywhere in the code to stop execution and get a debugger console
  gem 'byebug'
end

group :development do
  # Access an IRB console on exception pages or by using <%= console %> in views
  gem 'web-console', '~> 2.0'

  # Spring speeds up development by keeping your application running in the background. Read more: https://github.com/rails/spring
  gem 'spring'

  #active admin
  gem 'activeadmin', github: 'activeadmin'
  gem 'devise'
end
group :production do
 gem 'unicorn'
 gem 'pg'
 gem 'activeadmin', github: 'activeadmin'
 gem 'devise'
>>>>>>> 35917f1b83b79ff12cefad5d2cee1e048b39fc83
end
