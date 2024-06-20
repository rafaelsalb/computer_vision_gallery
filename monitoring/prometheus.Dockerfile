FROM prom/prometheus:v2.30.3
COPY prometheus.yml /etc/prometheus/prometheus.yml
EXPOSE 9090
ENTRYPOINT [ "prometheus", "--config.file=/etc/prometheus/prometheus.yml" ]