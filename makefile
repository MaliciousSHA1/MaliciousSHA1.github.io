NAMEIN=index
CSS=style.css
NAMEOUT=$(NAMEIN)

all:	$(NAMEIN).md $(CSS) 
	pandoc -s -S -H style.css $(NAMEIN).md -o $(NAMEOUT).html

clean:
	rm -rf $(NAMEIN)-*
