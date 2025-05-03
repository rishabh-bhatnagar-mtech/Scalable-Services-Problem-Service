include deployments/.env

create_secrets:
	export $$(xargs < deployments/.env) && \
	envsubst < deployments/k8s-secret.yaml > deployments/subst-secret.yaml && \
	kubectl apply -f deployments/subst-secret.yaml
	rm deployments/subst-secret.yaml

build_problem_image:
	docker build -t problem-service:"${PROBLEM_SERVICE_VERSION}" -f deployments/Dockerfile .

deploy_problem_service:
	export $$(xargs < deployments/.env) && \
	envsubst < deployments/problem-service.yaml > deployments/subst-problem-service.yaml
	kubectl apply -f deployments/subst-problem-service.yaml
	rm deployments/subst-problem-service.yaml

deploy_db_service:
	kubectl apply -f deployments/db-service.yaml

deploy: create_secrets build_problem_image deploy_db_service deploy_problem_service