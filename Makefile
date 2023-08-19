run:
	uvicorn server:app --reload

deploy:
	docker-compose up -d --build

deploy-db:
	docker-compose -f docker-compose.db.yml up -d --build