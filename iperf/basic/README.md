```bash
sudo RFSIMULATOR=server ./nr-softmodem -O gnb.sa.band78.106prb.rfsim.conf --parallel-config PARALLEL_SINGLE_THREAD --rfsim --phy-test
sudo RFSIMULATOR=127.0.0.1 ./nr-uesoftmodem --rfsim --phy-test --rrc_config_path .
```

