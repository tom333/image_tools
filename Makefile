clean: 
	rm -rf vue/dist vue/build web dist

vuecompile:
	cd vue && rm -rf dist/* && yarn run build --fix

vuedev:
	cd vue && npm run dev

webdata: vuecompile
	mkdir -p web && cp -r vue/dist/* web
