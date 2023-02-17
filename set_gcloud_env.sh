sed -i "s;__DATABSE_URI__;'$PROD_DATABSE_URI';" app.yaml
sed -i "s/__SECRET_KEY__/'$PROD_SECRET_KEY'/" app.yaml
sed -i "s/__JWT_SECRET_KEY__/'$PROD_JWT_SECRET_KEY'/" app.yaml
sed -i "s/__RANDOM_API_KEY__/'$PROD_RANDOM_API_KEY'/" app.yaml
