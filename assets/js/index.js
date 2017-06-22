var React = require('react')
var ReactDOM = require('react-dom')

var Hello = React.createClass ({
    render: function() {
        return (
            <h1>
            Change made so i can run my first codeship build!
            </h1>
        )
    }
})

ReactDOM.render(<Hello />, document.getElementById('container'))
