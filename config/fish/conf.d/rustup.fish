# curl https://sh.rustup.rs -sSf | sh -s -- --no-modify-path -y --default-toolchain none

function rustup --description "Rust versioning system"
  if test ! -x $HOME/.cargo/bin/rustup
    curl https://sh.rustup.rs -sSf | sh -s -- --no-modify-path -y --default-toolchain none
  end

  eval $HOME/.cargo/bin/rustup "$argv"
end
