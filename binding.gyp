{
    "targets": [
        {
            "target_name": "hashing",
            "sources": [
                "hashing.cpp",
                "yescrypt.c",
                "sha256_Y.c",
                "yescrypt-opt.c",
            ],
            "include_dirs": [
                "crypto",
            ],
            "cflags_cc": [
                "-std=c++0x"
            ],
        }
    ]
}
