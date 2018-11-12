import React, { Component } from 'react'

class SidebarComponent extends Component {
  constructor(props) {
    super(props)
    this.state = {

    }
  }

  render() {

    return (
      <div className="sidebar_container">
        <div className="top_contributors">
          top contributors
        </div>
        <div className="issues_resolved">
          issues resolved
        </div>
        <div className="member_count">
          member count
        </div>
        <div className="share_link">
          share link
        </div>
      </div>
    )
  }
}

export default SidebarComponent