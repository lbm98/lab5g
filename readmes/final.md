```bash
ssh lars@advnetlab-oai.idlab.uantwerpen.be
```

```bash
sudo docker compose stop oai-nr-ue oai-gnb
sudo docker compose up -d oai-gnb
sudo docker ps -a
sudo docker logs oai-amf
sudo docker logs oai-gnb
sudo docker compose up -d oai-nr-ue
```

```bash
git clone --depth 1 --branch 2023.w09 https://gitlab.eurecom.fr/oai/openairinterface5g
cd openairinterface5g/cmake_targets/
./build_oai -w SIMU --gNB -g Debug
cd ran_build/build
sudo ./nr-softmodem -O gnb.conf --sa -E --rfsim --log_config.global_log_options level,nocolor,time
```

```bash
git clone --depth 1 --branch 2023.w10 https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-fed
cd docker-compose
docker compose -f docker-compose-basic-nrf.yaml up -d
```

```bash
cmake -DRF_BOARD=OAI_SIMU -DCMAKE_BUILD_TYPE=Debug
```