mkdir -p ~/.streamlit/

#echo "/
#[general]\n\
#email = \"anatoly.danilevich@mail.de\"\n\
#" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
enableCORS = false
port = $PORT
" > ~/.streamlit/config.toml