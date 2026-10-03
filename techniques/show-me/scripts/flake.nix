{
  description = "Self-contained mdts browser viewer for the show-me skill";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = {
    self,
    nixpkgs,
  }: let
    systems = [
      "aarch64-darwin"
      "aarch64-linux"
      "x86_64-linux"
    ];
    forAllSystems = nixpkgs.lib.genAttrs systems;
  in {
    packages = forAllSystems (system: let
      pkgs = import nixpkgs {inherit system;};
    in {
      default = pkgs.buildNpmPackage {
        pname = "mdts";
        version = "0.20.6";
        src = ./mdts;
        npmDepsHash = "sha256-upjCEWTbFEDXdqnlcpQg7HSONvvWobyC1I5VHljsTrk=";
        dontNpmBuild = true;
      };
    });

    apps = forAllSystems (system: {
      default = {
        type = "app";
        program = "${self.packages.${system}.default}/bin/mdts";
        meta.description = "Serve local Markdown files in a browser";
      };
    });
  };
}
