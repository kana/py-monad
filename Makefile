TARGETS :=

test: $(TARGETS:%.py=,%.ok)

,%.ok: %.py
	python $<
	touch $@

# __END__
