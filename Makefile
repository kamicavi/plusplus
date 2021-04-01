# build local Jekyll pages
PORT := 4000

local: 
	bundle exec jekyll serve --port $(PORT)

build: 
	bundle exec jekyll build

check:
	bundle exec htmlproofer ./_site

check-internal:
	bundle exec htmlproofer ./_site --disable-external


debug: clean
	bundle exec jekyll build --verbose

clean:
	rm -rf _site/*
	@echo "cleaning _site"