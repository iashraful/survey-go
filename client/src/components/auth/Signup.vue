<template>
<section class="hero is-fullheight">
  <div class="hero-body">
    <div class="container" style="top: -10rem">
      <div class="columns is-centered">
        <div class="column is-5-tablet is-4-desktop is-3-widescreen">
          <h2 style="text-align: center; font-size: 1.5rem; margin-bottom: 5px;">Welcome to SurveyGo!</h2>
          <form action="" class="box">
            <div class="field">
              <label for="" class="label">Name</label>
              <div class="control has-icons-left">
                <input type="text" placeholder="e.g. John Smith" class="input" required>
                <span class="icon is-small is-left">
                  <i class="fa fa-human"></i>
                </span>
              </div>
            </div>
            <div class="field">
              <label for="" class="label">Email</label>
              <div class="control has-icons-left">
                <input type="email" placeholder="e.g. bobsmith@gmail.com" class="input" required>
                <span class="icon is-small is-left">
                  <i class="fa fa-envelope"></i>
                </span>
              </div>
            </div>
            <div class="field">
              <label for="" class="label">Password</label>
              <div class="control has-icons-left">
                <input type="password" placeholder="*******" class="input" required>
                <span class="icon is-small is-left">
                  <i class="fa fa-lock"></i>
                </span>
              </div>
            </div>
            <div class="field">
              <label for="" class="label">Confirm Password</label>
              <div class="control has-icons-left">
                <input type="password" placeholder="*******" class="input" required>
                <span class="icon is-small is-left">
                  <i class="fa fa-lock"></i>
                </span>
              </div>
            </div>
            <div class="field">
              <button class="button is-success is-fullwidth">
                Signup
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>
</template>
