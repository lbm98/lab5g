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