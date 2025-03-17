{
  pkgs ? import <nixpkgs> { },
}:
pkgs.mkShell {
  # nativeBuildInputs is usually what you want -- tools you need to run
  nativeBuildInputs = with pkgs.buildPackages; [
    pkg-config
    freetype
    fontconfig
    (pkgs.python3.withPackages (ps: with ps; [
      pandas
      numpy
      scipy
      networkx
      matplotlib
      black
    ]))
  ];
}
