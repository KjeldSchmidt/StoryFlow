const game_id = document.getElementById( 'game_editor' ).dataset.game_id;


/*


	STORY PANEL CODE HERE


 */


/**
 *     Attaches a submit handler to the currently active story form, which
 *    POSTs the story panel to save all changes.
 */
function attach_submit_story_handler() {
	const story_edit_form = document.getElementById( 'story_edit_form' );
	story_edit_form.addEventListener( 'submit', function ( event ) {
		event.preventDefault();
		const data = {
			'text': story_edit_form.text.value,
			'name': story_edit_form.name.value,
			'comment': story_edit_form.comment.value,
		};

		const url = story_edit_form.action;
		postAjax( url, validate_story_submit_success, data );
	} );
}

function validate_story_submit_success( response ) {
	const new_story_name = document.getElementById( 'story_edit_form' ).name.value;
	story_link_currently_edited.innerText = new_story_name;
}


/*


	FLOW PANEL CODE HERE


 */

let story_link_currently_edited = undefined;

/**
 * Attaches a handler to all story links in the flow panel
 * which loads a complete form into the story panel when clicked.
 */
document.querySelectorAll( '#story_flow_overview .story_link' ).forEach( function ( elem ) {
	add_story_load_handler( elem );
} );

/**
 * Attaches a handler to all story links in the flow panel for dragging them around
 */

document.querySelectorAll( '#story_flow_overview .story_link' ).forEach( function ( elem ) {
	$( elem ).draggable( {
		containment: '#story_flow_overview',
		
		stop: function ( event, ui ) {
			const story_id = event.target.dataset.story_id;
			const url = '/game/' + game_id + '/edit/story/' + story_id + "/move";
			const data = {
				x_position: ui.position.left,
				y_position: ui.position.top
			};
			postAjax( url, undefined, data )
		}
	} );
} );


/**
 * Attaches a handler to the create new story button
 * which calls on the server to create a new story and loads it into the flow and story panels.
 */
document.getElementById( 'create_new_story_button' ).addEventListener( 'click', function ( event ) {
	event.preventDefault();
	const target_url = event.target.parentNode.href;
	getAjax( target_url, attach_new_story_to_edit_panel );
} );

/**
 * Attaches a click handler to a story link in the flow handler, which loads a story edit form
 *
 * @param elem The story link to which the event should be attached.
 */
function add_story_load_handler( elem ) {
	elem.addEventListener( 'click', function ( event ) {
		const story_link = event.target;
		const story_id = story_link.dataset.story_id;
		const url = '/game/' + game_id + '/edit/story/' + story_id;

		story_link_currently_edited = story_link;
		getAjax( url, attach_story_to_edit_panel );
	} );
}

/**
 * Attaches a story form to the story panel
 *
 * @param html_string The html string for the story form.
 */
function attach_story_to_edit_panel( html_string ) {
	document.getElementById( 'game_editor_story_panel' ).innerHTML = html_string;
	attach_submit_story_handler();
}

/**
 * Creates a new story link in the flow panel and attaches a story form to the story panel.
 *
 * @param html_string The html string for the story form.
 */
function attach_new_story_to_edit_panel( html_string ) {
	document.getElementById( 'game_editor_story_panel' ).innerHTML = html_string;

	const story_form = document.getElementById( 'story_edit_form' );
	const new_story_name = story_form.name.value;
	const new_story_id = story_form.dataset.story_id;

	const new_story_link = add_story_link( new_story_id, new_story_name );
	story_link_currently_edited = new_story_link;
	attach_submit_story_handler();
}

/**
 * Adds a story link to the flow panel
 *
 * @param story_id ID of the story to be added
 * @param story_name Name of the story to be added
 */
function add_story_link( story_id, story_name ) {
	const story_link_template = document.getElementById( 'story_link_template' );
	const new_story_link = document.importNode( story_link_template.content, true ).querySelector( '.story_link' );
	console.dir( new_story_link );
	new_story_link.dataset.story_id = story_id;
	new_story_link.innerText = story_name;
	add_story_load_handler( new_story_link );

	const flow_overview = document.getElementById( 'story_flow_overview' );
	flow_overview.appendChild( new_story_link );

	return new_story_link;
}