export_secrets:
	export $(xargs < deployments/.env) && envsubst < deployments/k8s-secret.yaml > deployments/subst-secret.yaml

deploy:
	kubectl apply -f deployments/db-service.yaml
	kubectl apply -f deployments/k8s-secret.yaml
	kubectl apply -f deployments/problem-service.yaml