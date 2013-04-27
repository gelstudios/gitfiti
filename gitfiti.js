var color = [
  'rgb(255, 255, 255)',
  'rgb(200, 255, 255)',
  'rgb(150, 255, 255)',
  'rgb(100, 255, 255)',
  'rgb(50, 255, 255)',
  'rgb(0, 255, 255)',
]

var paint=0
document.body.addEventListener('mousedown', function(){paint=1;console.log('painting');}, false );
document.body.addEventListener('mouseup',function(){paint=0;console.log('released')}, false);

function box(){
	var box = document.createElement("div");
	box.value=0;
	box.style.width='25px';
	box.style.height='25px';
	box.style.border='1px solid gray';
	box.style.backgroundColor=color[0];
	box.paint=0
	//box.onclick = function() { cycle(this);};
	box.addEventListener('mousemove', function(){cycle(this);}, false );
	document.body.appendChild(box);
	return box
};

function boxes(){
	var column = [];
	for (i=0;i<7;i++){
		column[i]=box();
	}
}

function cycle(object){
	if (paint==1){
	object.value+=0.5;
	object.value%6;
	object.style.backgroundColor=color[object.value];
	}
}

boxes();