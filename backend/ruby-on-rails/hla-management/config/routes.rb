Rails.application.routes.draw do
  devise_for :users, # generate devise router by reference to User
             path: '', # path set to '', deafult /users/
             path_names: {
              sign_in: 'login', # sign_in -> login
              sign_out: 'logout', # sign_out -> logout
              registration: 'signup' # sign_up -> signup
             },
             controllers:{ # use custom controller to replace default controllers
              sessions: 'users/sessions', 
              registrations: 'users/registrations'
             }

  resources :users
  ## API
  ## GET    /users          -> users#index
  ##GET    /users/:id      -> users#show
  ##POST   /users          -> users#create
  ##PUT    /users/:id      -> users#update
  ##PATCH  /users/:id      -> users#update
  ##DELETE /users/:id      -> users#destroy

  mount Rswag::Ui::Engine => '/api-docs'
  mount Rswag::Api::Engine => '/api-docs'
  get "up" => "rails/health#show", as: :rails_health_check
end
