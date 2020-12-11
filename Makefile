docker: Dockerfile
	docker build -t sus .
	docker run -it sus .