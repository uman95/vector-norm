mkdir -p ~/.streamlit/
echo "[general]"  > ~/.streamlit/credentials.toml
echo "email = \"usman.aganiy@gmail.com\""  >> ~/.streamlit/credentials.toml
echo "[server]"  > ~/.streamlit/config.toml 
echo "headless = true"  >> ~/.streamlit/config.toml
echo "port = $PORT"  >> ~/.streamlit/config.toml
echo "enableCORS = false"  >> ~/.streamlit/config.toml


# mkdir -p ~/.streamlit/echo "\
# [server]\n\
# headless = true\n\
# port = $PORT\n\
# enableCORS = false\n\
# \n\
# " > ~/.streamlit/config.toml