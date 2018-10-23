class Draggable {
	constructor( element, boundary ) {
		this.element = element;
		this.boundary = boundary;

		this.element.addEventListener( 'mousedown', this.start_following() );
		document.addEventListener( 'mouseup', this.stop_following() );
	}

	follow_mouse() {
		const boundary = this.boundary;
		const drag_element = this.element;

		this.move_listener = function ( event ) {
			const x = event.pageX;
			const y = event.pageY;
			const x_offset = boundary.offsetLeft;
			const y_offset = boundary.offsetTop;

			drag_element.style.left = x - x_offset;
			drag_element.style.top = y - y_offset;
		};
		return this.move_listener;
	}

	start_following() {
		const follow_mouse = this.follow_mouse();
		return function ( event ) {
			document.addEventListener( 'mousemove', follow_mouse );
		}
	}

	stop_following() {
		const listener = this.move_listener;
		return function () {
			document.removeEventListener( 'mousemove', listener );
		}
	}
}

document.addEventListener( 'click', ( event ) => console.log( event.pageX + ", " + event.pageY ) );