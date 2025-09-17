{
  description = "A flake for informatics projects/homework with python 3.12 for CS:5110";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        python = pkgs.python312;
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            python
            basedpyright
            uv
            zsh
            zsh-completions
            readline
            ncurses
            which
            findutils
            tree
          ];

          shellHook = ''
            echo "setting up shell..."
            export SHELL=${pkgs.zsh}/bin/zsh
            echo "Using Python $(python --version) with uv $(uv --version)"
            
            if [ -f "uv.lock" ]; then
              echo "Syncing from uv.lock..."
              uv sync
            else
              echo "Initializing..."
              uv init
              uv lock
              uv sync
            fi
            
            source .venv/bin/activate
            echo "Ready!"
          '';

          UV_CACHE_DIR = ".nix-uv-cache";
        };
      }
    );
}
