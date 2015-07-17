require "sinatra"
require "sinatra/json"
require "sinatra/reloader"

class HelloWorld < Sinatra::Base
  configure :development do
    register Sinatra::Reloader
  end

  get "/" do
    "sinatra root..."
  end

  get "/j" do
    h = {a: "A", b: "B"}
    json h
  end

end

HelloWorld.run!
