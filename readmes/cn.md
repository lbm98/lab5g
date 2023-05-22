```bash
docker rm -vf $(docker ps -aq)
docker rmi -f $(docker images -aq)
```

```bash
git clone --depth 1 --branch 2023.w10 https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-fed
cd oai-cn5g-fed/docker-compose
```

```bash
docker compose -f docker-compose-basic-nrf.yaml up
```

```bash
docker ps
```

https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-fed/-/blob/2023.w10/docs/CONFIGURE_CONTAINERS.md
```
mysql --> oai-nrf --> oai-udr --> oai-udm --> oai-ausf --> oai-amf --> oai-smf --> oai-upf
```

Enter the data network
```bash
docker exec -it oai-ext-dn bash
```

Check a table from the MySLQ database
```bash
mysql -h 192.168.70.131 -P 3306 -utest -ptest -e "USE oai_db; SELECT * FROM AuthenticationSubscription LIMIT 3"
```

