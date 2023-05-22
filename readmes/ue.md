## Sources

- [build](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/doc/BUILD.md)


```bash
git clone --depth 1 --branch 2023.w09 https://gitlab.eurecom.fr/oai/openairinterface5g
```

```bash
./build_oai -w SIMU --enb ...
```

```bash
cd openairinterface5g/cmake_targets/
./build_oai -I
sudo apt install zlib1g-dev
./build_oai -w SIMU --nrUE
```

```bash
sudo ./ran_build/build/nr-uesoftmodem -r 106 --numerology 1 --band 78 -C 3619200000 --ssb 516 --sa
```

```bash
./build_oai -w SIMU --gNB
```