practica.zip: src/jsbach.g4 src/jsbach.py README.md
	zip -j practica.zip src/jsbach.g4 src/jsbach.py README.md

clean: 
	rm practica.zip

##@ Understand (knowledge graph)

.PHONY: understand-dashboard
understand-dashboard: ## Launch the Understand Anything knowledge-graph dashboard (graph dir = repo root)
	@node -e "require(require('os').homedir()+'/.understand-anything/repo/understand-anything-plugin/packages/dashboard/launch.cjs')"
