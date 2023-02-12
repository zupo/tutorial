let
  nixpkgs = builtins.fetchTarball {
    # https://status.nixos.org/ -> nixos-22.11 on 2023-02-10
    url = "https://github.com/nixos/nixpkgs/archive/49efda9011e8cdcd6c1aad30384cb1dc230c82fe.tar.gz";
  };
  pkgs = import nixpkgs {};
  poetry2nix = import (fetchTarball {
    # https://github.com/nix-community/poetry2nix/commits/master on 2023-02-10
    url = "https://github.com/nix-community/poetry2nix/archive/860530598f2ab9a9a0e89dc79851d14b0aed3bf7.tar.gz";
  }) {
    pkgs = pkgs;
  };

  env = poetry2nix.mkPoetryEnv {
    pyproject = ./pyproject.toml;
    poetrylock = ./poetry.lock;
    editablePackageSources = {
      tutorial = ./.;
    };
  };
in

pkgs.mkShell {
  name = "dev-shell";
  buildInputs = [
    env
    pkgs.poetry
    pkgs.heroku
  ];

}
