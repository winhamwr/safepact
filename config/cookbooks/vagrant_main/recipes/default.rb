require_recipe "apt"
require_recipe "apache2"
require_recipe "mysql"

include_recipe 'python'

execute "disable-default-site" do
  command "sudo a2dissite default"
  notifies :reload, resources(:service => "apache2"), :delayed
end

web_app "project" do
  template "project.conf.erb"
  notifies :reload, resources(:service => "apache2"), :delayed
end

package "git-core" do
  action :install
end

package "vim" do
  action :install
end

execute "install-virtualenv" do
  command "easy_install virtualenv"
end

execute "make-virtualenv" do
  command "virtualenv #{node[:vagrant][:directory]}/.virtualenv"
end

execute "install-pip" do
  command "#{node[:vagrant][:directory]}/.virtualenv/bin/easy_install pip"
end

execute "install-base-reqs" do
  command "#{node[:vagrant][:directory]}/.virtualenv/bin/pip install -r #{node[:vagrant][:directory]}/safepact/requirements/base.txt"
end

execute "install-project-reqs" do
  command "#{node[:vagrant][:directory]}/.virtualenv/bin/pip install -r #{node[:vagrant][:directory]}/safepact/requirements/project.txt"
end

template "bashrc" do
  path "/home/vagrant/.bashrc"
  source "bashrc.erb"
  owner "vagrant"
  group "vagrant"
  mode 0644
end
