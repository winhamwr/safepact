Vagrant::Config.run do |config|
  config.vm.box = "lucid32"

  config.vm.provision :chef_solo do |chef|
    chef.cookbooks_path = ["config/site-cookbooks/opscode", "config/cookbooks"]
    chef.add_recipe("vagrant_main")
  end

  config.vm.network("192.168.10.10")
  config.vm.forward_port "http", 8000, 8800

  config.vm.share_folder("v-root", "/opt/safepact/versions/current", ".", :nfs => true)

end
