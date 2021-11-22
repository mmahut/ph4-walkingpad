with import <nixpkgs> {};
(let
  ph4-acmd2 = python38.pkgs.buildPythonPackage rec {
    pname = "ph4-acmd2";
    version = "0.0.5";

    buildInputs = [ python38.pkgs.cmd2 ];

    src = python38.pkgs.fetchPypi {
      inherit pname version;
      sha256 = "sha256-W//qwqjPQ1B8oR4YfceBytnl1VI7U4fu+ZfW9G9mgkg=";
    };
  };

  in python38.withPackages (ps: [
      ps.coloredlogs
      ps.aioconsole
      ps.cmd2
      ps.blessed
      ps.bleak
      ps.requests
      ps.dbus-python
      ph4-acmd2
    ])
).env