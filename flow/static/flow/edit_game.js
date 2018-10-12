let story_link_currently_edited = undefined;

/*
	Make all story links in the flow panel able to load in the story panel.
 */
document.querySelectorAll( '#story_flow_overview .story_link' ).forEach( function ( elem ) {
	const game_id = document.getElementById( 'game_editor' ).dataset.game_id;

	elem.addEventListener( 'click', function ( event ) {
		const story_link = event.target;
		const story_id = story_link.dataset.story_id;
		const url = '/game/' + game_id + '/edit/story/' + story_id;

		story_link_currently_edited = story_link;
		getAjax( url, attach_story_to_edit_panel );
	} );
} );

function attach_story_to_edit_panel( html_string ) {
	document.getElementById( 'game_editor_story_panel' ).innerHTML = html_string;
	set_submit_button_function();
}

/*
	Submit button for story saving.
 */

function set_submit_button_function() {
	const story_edit_form = document.getElementById( 'story_edit_form' );
	story_edit_form.addEventListener( 'submit', function ( event ) {
		event.preventDefault();
		const data = {
			'text': story_edit_form.text.value,
			'name': story_edit_form.name.value,
			'comment': story_edit_form.comment.value,
		};

		const url = story_edit_form.action;
		console.log( url );
		postAjax( url, validate_story_submit_success, data );
	} );
}

function validate_story_submit_success( response ) {
	const new_story_name = document.getElementById( 'story_edit_form' ).name.value;
	story_link_currently_edited.innerText = new_story_name;
}