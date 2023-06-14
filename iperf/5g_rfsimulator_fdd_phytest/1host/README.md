Terminal 1
```bash
docker exec -it rfsim5g-oai-gnb bash
ping -I oaitun_enb1 10.0.1.2
```

Terminal 2
```bash
docker exec -it rfsim5g-oai-nr-ue bash
ping -I oaitun_ue1 10.0.1.1
```