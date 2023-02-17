DATABSE_URI=postgresql://wgpkpnzw:Qby5jTOWQ5Ygs6uCQ6iZdVo7SnzGGYpr@otto.db.elephantsql.com/wgpkpnzw
SECRET_KEY=jnNGBu9ipdi4RuuHo8R3NwAd6Po=
JWT_SECRET_KEY=MHXeDG0h+TGH0GDwYtEerc5fCTY=
RANDOM_API_KEY=06b9fa5c-6d04-4056-aff4-62a864f76b46

echo "$DATABSE_URI"

sed -i "s;__DATABSE_URI__;'$DATABSE_URI';" app.yaml
sed -i "s/__SECRET_KEY__/'$SECRET_KEY'/" app.yaml
sed -i "s/__JWT_SECRET_KEY__/'$JWT_SECRET_KEY'/" app.yaml
sed -i "s/__RANDOM_API_KEY__/'$RANDOM_API_KEY'/" app.yaml
