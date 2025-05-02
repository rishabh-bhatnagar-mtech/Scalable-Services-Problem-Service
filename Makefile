export_secrets:
	export $$(xargs < deployments/.env) && \
	envsubst < deployments/k8s-secret.yaml > deployments/subst-secret.yaml && \
	kubectl apply -f deployments/subst-secret.yaml
	rm deployments/subst-secret.yaml

deploy_services:
	kubectl apply -f deployments/db-service.yaml
	kubectl apply -f deployments/k8s-secret.yaml
	kubectl apply -f deployments/problem-service.yaml

deploy: export_secrets deploy_services