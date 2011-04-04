TARGETS := monad.py maybe.py

test: $(TARGETS:%.py=,%.ok)

,%.ok: %.py
	python $<
	touch $@

# __END__
