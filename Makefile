run:
	uvicorn server:app --reload

deploy:
	docker-compose up -d --build