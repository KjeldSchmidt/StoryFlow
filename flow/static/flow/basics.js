if ( !Array.prototype.last ) {
	Array.prototype.last = function () {
		return this[ this.length - 1 ];
	};
}
;

function buildDataString( data ) {
	if ( data === undefined ) {
		return '';
	}
	return Object.keys( data ).map(
		function ( k ) {
			return encodeURIComponent( k ) + '=' + encodeURIComponent( data[ k ] )
		},
	).join( '&' );
}

function getAjax( url, callback, data ) {
	let dataString = buildDataString( data );
	let data_url = ( dataString === '' ) ? url : url + '?' + dataString;
	let xmlhttp;

	xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function () {
		if ( xmlhttp.readyState === 4 && xmlhttp.status === 200 ) {
			callback( xmlhttp.responseText );
		}
	};
	xmlhttp.open( 'GET', data_url, true );

	xmlhttp.send();
}

function postAjax( url, callback, data ) {
	let dataString = buildDataString( data );
	let xmlhttp;

	xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function () {
		if ( xmlhttp.readyState === 4 && xmlhttp.status === 200 ) {
			callback( xmlhttp.responseText );
		}
	};
	xmlhttp.open( 'POST', url, true );

	let csrftoken = Cookies.get( 'csrftoken' );
	xmlhttp.setRequestHeader( 'X-CSRFToken', csrftoken );
	xmlhttp.setRequestHeader( 'content-type', 'application/x-www-form-urlencoded' );

	xmlhttp.send( dataString );
}