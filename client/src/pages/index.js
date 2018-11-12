import React from 'react'
// import { Link } from 'gatsby'
import Layout from '../components/layout'
import Issues from '../components/issues'
import Sidebar from '../components/sidebar'

class IndexPage extends React.Component {
  
  render() {
    return (
      <Layout>
        <Issues></Issues>
        <Sidebar></Sidebar>
      </Layout>
    )
  }
} 

export default IndexPage
