 
{ pkgs }: {
  deps = [
    pkgs.imagemagick6_light
pkgs.python38Full
  ];
  env = {
    PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
    LANG = "en_US.UTF-8";
  };
}
# { pkgs }: {
#   deps = [
#     pkgs.imagemagick6_light
# pkgs.>>> channel_layer = channels.layers.get_channel_layer()
# pkgs.python38Full
#   ];
#   env = {
#     PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
#     LANG = "en_US.UTF-8";
#   };
# }