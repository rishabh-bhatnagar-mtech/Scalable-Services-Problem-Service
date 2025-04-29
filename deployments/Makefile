export_secrets:
	export $(xargs < .env)
	envsubst < k8s-secret.yaml